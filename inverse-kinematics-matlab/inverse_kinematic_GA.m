%% Inverse Kinematics using Geometric Algebra reference: 
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