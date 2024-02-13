%% FK using CCA

% Initialising conformal signature (3,0)
% Initialising Clifford  signature (4,1)
conformal_signature(3,0);

a0 = 2; a1 = 2;
theta0 = 0; theta1 = 45; theta2 = 35;

fprintf('R _|_ R || R configuration, with angles %d, %d & %d',theta0, theta1, theta2);

R0 = rotor(deg2rad(theta0),e1,e3);
R1 = rotor(deg2rad(theta1),e1,e2);
T1 = 
EE1 = Rbase*(a0*e1)*reverse(Rbase);

R2 = rotor(deg2rad(theta2),e1,e2);
R02 = Rbase*R2;
EE2 = EE1 + R02*(a1*e1)*reverse(R02);

display(EE2);

% Defining a rotor
% angle of rotation in radian. 
% mv1: vector that needs to be rotated. 
% mv2: vector that mv1 is to be rotated about.
function R = rotor(angle,mv1,mv2)
    % Normalised the multivector1, i.e, the initial vector
    mv1 = unit(mv1);% or mv1 = mv1/abs(mv1);
    % Normalised the multivector1, i.e, the final rotated vector
    mv2 = unit(mv2); % or mv2 = mv2/abs(mv2);
    
    mv1WedgeMv2 = mv1*mv2; %creating a bi-vector
    mv1WedgeMv2 = unit(mv1WedgeMv2); % or mv1WedgeMv2 = mv1WedgeMv2/abs(mv1WedgeMv2)

    R = cos(angle/2) - mv1WedgeMv2*sin(angle/2);

end