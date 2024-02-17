%% Inverse Kinematics using Homogeneous Matrix
%% R configuration

clear all;clc;
display('R configuration...');

syms a0 the0
a0 = 2; %2 units lenght
t1= 45;

H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H = H01;

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])
px=vpa(subs(H01(1,4),[the0,a0],[t1,a0]));
py=vpa(subs(H01(2,4),[the0,a0],[t1,a0]));
pz=vpa(subs(H01(3,4),[the0,a0],[t1,a0]));
% fprintf("Expected position: %d %d %d \n",px,py,pz);
fprintf("Expected value(s): %d \n",t1);

theta0 = solve(H01(1,4)==px,the0);
solution = [theta0];
fprintf("Calculated solution for IK is(are):\n")
disp(theta0);