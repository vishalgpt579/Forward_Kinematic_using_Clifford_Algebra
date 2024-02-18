%% Forward Kinematic of serial-manipulator 
% in different configurations
% using Geometric Algebra
% with the help of Clifford Multivector Toolbox library.

disp('Initialising Clifford signature (3,0)');
clifford_signature(3,0);

% Testing simple Reflection of x =(1,1) on y=0 or y-axis
x= 1*e1+1*e2; % or 
% clifford(0,1,1,0,0,0,0,0)
% ans = 
% 
%    0.0000 e0 
%  + 1.0000 e1  + 1.0000 e2  + 0.0000 e3 
%  + 0.0000 e12 + 0.0000 e13 + 0.0000 e23
%  + 0.0000 e123
reflector = e2; %across the y-axis
x_bar = reflector*(x)*reverse(reflector);
fprintf('Original vector: ');
disp(x);
fprintf('Reflector vector across y-axis: ');
disp(x_bar);

%% R configuration

clear all;clc;
disp('Initialising Clifford signature (3,0)')
clifford_signature(3,0);

a0 = 2; % unit length
theta0 = 45;
fprintf('R configuration, with angle %d',theta0);

% Computing the Rotor of joint-0
R0 = rotor(deg2rad(theta0),e1,e2);
EE0 = R0*(a0*e1)*reverse(R0);

display(EE0);

%% R || R configuration

clear all;clc;
disp('Initialising Clifford signature (3,0)')
clifford_signature(3,0);

a0 = 2; %2 units lenght
a1 = 2;
theta0 = 45;
theta1 = 30;
fprintf('R || R configuration, with angles %d & %d',theta0, theta1);

R0 = rotor(deg2rad(theta0),e1,e2);
EE0 = R0*(a0*e1)*reverse(R0);

R1 = rotor(deg2rad(theta1),e1,e2);
R01 = R0*R1;
EE1 = EE0 + R01*(a1*e1)*reverse(R01);

display(EE1);

%% R || R || R configuration

clear all;clc;
disp('Initialising Clifford signature (3,0)')
clifford_signature(3,0);

a0 = 2; a1 = 2; a2 = 2; %2 units lenght
theta0 = 45; theta1 = 30; theta2 = -45;

fprintf('R || R || R configuration, with angles %d, %d & %d',theta0, theta1, theta2);

R0 = rotor(deg2rad(theta0),e1,e2);
EE0 = R0*(a0*e1)*reverse(R0);

R1 = rotor(deg2rad(theta1),e1,e2);
R01 = R0*R1;
EE1 = EE0 + R01*(a1*e1)*reverse(R01);

R2 = rotor(deg2rad(theta2),e1,e2);
R02 = R01*R2;
EE2 = EE1 + R02*(a2*e1)*reverse(R02);

display(EE2);

%% R _|_ R configuration

% clear all;clc;
disp('Initialising Clifford signature (3,0)')
clifford_signature(3,0);

a0 = 2; %2 units lenght
a1 = 2;
theta0 = 0;
theta1 = 30;
fprintf('R _|_ R configuration, with angles %d & %d',theta0, theta1);

R0 = rotor(deg2rad(theta0),e1,e3);
EE0 = R0*(a0*e2)*reverse(R0);

R1 = rotor(deg2rad(theta1),e1,e2);
R01 = R0*R1;
EE1 = EE0 + R01*(a1*e1)*reverse(R01);

display(EE1);

%% R _|_ R || R configuration 
% from clifford example:https://slides.com/hugohadfield/game2020#/18 

clear all;clc;
disp('Initialising Clifford signature (3,0)')
clifford_signature(3,0);

a0 = 2; a1 = 2;
theta0 = 0; theta1 = 45; theta2 = 35;

fprintf('R _|_ R || R configuration, with angles %d, %d & %d',theta0, theta1, theta2);

R0 = rotor(deg2rad(theta0),e1,e3);
R1 = rotor(deg2rad(theta1),e1,e2);
Rbase = R0*R1;
EE1 = Rbase*(a0*e1)*reverse(Rbase);

R2 = rotor(deg2rad(theta2),e1,e2);
R02 = Rbase*R2;
EE2 = EE1 + R02*(a1*e1)*reverse(R02);

display(EE2);
%% Defining a rotor
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