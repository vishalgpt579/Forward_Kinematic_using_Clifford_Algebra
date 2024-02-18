%% FK using CCA (NOT WORKING!!!)

% Initialising conformal signature (3,0)
% Initialising Clifford  signature (4,1)
conformal_signature(3,0);
tool = clifford_tools_local;
% λ value:  1
% Origin:   eo = - 0.7071 e4    + 0.7071 e5
% Infinity: e∞ = 0.7071 e4    + 0.7071 e5   = ei
% Bivector: E  = 0.7071 e4    + 0.7071 e5 

a0 = 2; a1 = 2;
theta0 = 0; theta1 = 45; theta2 = 35;

fprintf('R _|_ R || R configuration, with angles %d, %d & %d',theta0, theta1, theta2);

R0 = tool.rotor(deg2rad(theta0),e1,e3);
R1 = tool.rotor(deg2rad(theta1),e1,e2);
T1 = 1 - 0.5*a0*(e1*ei); % or T1 = 1-0.5*(e1*(0.7071*e4+0.7071*e5))
R2 = tool.rotor(deg2rad(theta2),e1,e2);
T2 = 1 - 0.5*a1*(e1*ei);
R = R0*R1*T1*R2*T2;

EE = tool.down(R*tool.up(eo)*reverse(R));
fprintf("\nThe End-effector is at: ");
disp(EE);

%% Functions
% % Defining a rotor
% % angle of rotation in radian. 
% % mv1: vector that needs to be rotated. 
% % mv2: vector that mv1 is to be rotated about.
function R = rotor(angle,mv1,mv2)
    % Normalised the multivector1, i.e, the initial vector
    mv1 = unit(mv1);% or mv1 = mv1/abs(mv1);
    % Normalised the multivector1, i.e, the final rotated vector
    mv2 = unit(mv2); % or mv2 = mv2/abs(mv2);
    
    mv1WedgeMv2 = mv1*mv2; %creating a bi-vector
    mv1WedgeMv2 = unit(mv1WedgeMv2); % or mv1WedgeMv2 = mv1WedgeMv2/abs(mv1WedgeMv2)

    R = cos(angle/2) - mv1WedgeMv2*sin(angle/2);
end

% % Defining function to 
% % convert vector to multivector: up
% % Reconvert a multivector to vector: down
% % Reference: https://clifford.readthedocs.io/en/latest/tutorials/cga/index.html

% Project a multivector to conformal space (GA-->CGA)
function mv_conformal = up(mv)
    mv_conformal = mv + (0.5*(mv^2)*ei) + eo;
end

% Projection from CGA to GA
function mv = down(mv_conformal)
    mv_conformal = unit(mv_conformal);
    mv = mv_conformal*eo*inv(eo);
end