%% Inverse Kinematics using Homogeneous Matrix
%% R configuration

% clear all;clc;
display('R configuration...');

syms a0 the0
a0 = 2; %2 units lenght
t1= 45;

H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H = H01;

% Computing the EE's Px, Py & Pz(essentially the forward kinematics)
px=vpa(subs(H01(1,4),[the0,a0],[t1,a0]));
py=vpa(subs(H01(2,4),[the0,a0],[t1,a0]));
pz=vpa(subs(H01(3,4),[the0,a0],[t1,a0]));
% fprintf("Expected position: %d %d %d \n",px,py,pz);
fprintf("Expected value(s): %d \n",t1);
fprintf("Solving Inverse Kinematics(IK)...\n");
theta0 = solve(H01(1,4)==px,the0);
solution = [theta0];
fprintf("Calculated solution for IK is(are):\n")
disp(theta0);

%% R || R configuration

syms a0 a1 the0 the1;
disp('R || R configuration...');
a0 = 2; a1 = 2;
t1 = 45; t2 = 30;

H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H12= [cosd(the1) -sind(the1) 0 a1*cosd(the1);...
      sind(the1)  cosd(the1) 0 a1*sind(the1);...
      0         0      1    0;...
      0         0      0    1];

H = simplify(H01*H12);

% Computing the EE's Px, Py & Pz(essentially the forward kinematics)
px=vpa(subs(H(1,4),[the0,the1],[t1,t2]));
py=vpa(subs(H(2,4),[the0,the1],[t1,t2]));
pz=vpa(subs(H(3,4),[the0,the1],[t1,t2]));

% fprintf("Expected position: %d %d %d \n",px,py,pz);
fprintf("Expected value(s) for theta0: %d & theta2: %d \n",t1,t2);
fprintf("Solving Inverse Kinematics(IK)...\n");
[theta0,theta1] = solve(H(1,4)==px,H(2,4)==py,the0,the1);
solution = [theta0,theta1];
fprintf("Calculated solution for IK is(are):\n")
disp(solution);

%% R || R || R
clear all; clc;
disp('R || R || R configuration...');
syms the0 the1 the2;

% System Configuration...
a0 = 2; a1 = 2; a2 = 2; %links lengths
t1 = 45; t2 = 30; t3 = -45; %test Angles (or expected angles)

H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H12= [cosd(the1) -sind(the1) 0 a1*cosd(the1);...
      sind(the1)  cosd(the1) 0 a1*sind(the1);...
      0         0      1    0;...
      0         0      0    1];

H23= [cosd(the2) -sind(the2) 0 a2*cosd(the2);...
      sind(the2)  cosd(the2) 0 a2*sind(the2);...
      0         0      1    0;...
      0         0      0    1];

H = simplify(H01*H12*H23);

% Computing the EE's Px, Py & Pz(essentially the forward kinematics)
px=vpa(subs(H(1,4),[the0,the1,the2],[t1,t2,t3]));
py=vpa(subs(H(2,4),[the0,the1,the2],[t1,t2,t3]));
pz=vpa(subs(H(3,4),[the0,the1,the2],[t1,t2,t3]));

% fprintf("Expected position: %d %d %d \n",px,py,pz);
fprintf("Expected value(s) for theta0: %d, theta1 = %d & theta2: %d  \n",t1,t2,t3);
fprintf("Solving Inverse Kinematics(IK)...\n");

[theta0,theta1,theta2] = solve(H(1,4)==px,H(2,4)==py,H(3,4)==pz,the0,the1,the2);
solution = [vpa(theta0),vpa(theta1),vpa(theta2)];

fprintf("Calculated solution for IK is(are):\n")
disp(solution);
%% R || R || R 2nd attempt using radian angles.
clear all; clc;
disp('R || R || R configuration...');
syms the0 the1 the2;

% System Configuration...
a0 = 2; a1 = 2; a2 = 2; %links lengths

t1 = 45; t2 = 30; t3 = -45; %test Angles (or expected angles)
fprintf("Expected value(s) for theta0: %d, theta1 = %d & theta2: %d  \n",t1,t2,t3);
t1=deg2rad(t1); t2=deg2rad(t2); t3=deg2rad(t3);

H01 = [cos(the0) -sin(the0) 0 a0*cos(the0);...
      sin(the0)  cos(the0) 0 a0*sin(the0);...
      0         0      1    0;...
      0         0      0    1];

H12= [cos(the1) -sin(the1) 0 a1*cos(the1);...
      sin(the1)  cos(the1) 0 a1*sin(the1);...
      0         0      1    0;...
      0         0      0    1];

H23= [cos(the2) -sin(the2) 0 a2*cos(the2);...
      sin(the2)  cos(the2) 0 a2*sin(the2);...
      0         0      1    0;...
      0         0      0    1];

H = simplify(H01*H12*H23);

% Computing the EE's Px, Py & Pz(essentially the forward kinematics)
px=vpa(subs(H(1,4),[the0,the1,the2],[t1,t2,t3]));
py=vpa(subs(H(2,4),[the0,the1,the2],[t1,t2,t3]));
pz=vpa(subs(H(3,4),[the0,the1,the2],[t1,t2,t3]));

% fprintf("Expected position: %d %d %d \n",px,py,pz);
fprintf("Solving Inverse Kinematics(IK)...\n");
[theta1,theta2,theta3] = solve(H(1,4)==px,H(2,4)==py,H(3,4)==pz,the0,the1,the2);
% solve(H(1,4)==px,H(2,4)==py,H(3,4)==pz,the0,the1,the2);

Theta1=vpa(rad2deg(theta1));
Theta2=vpa(rad2deg(theta2));
Theta3=vpa(rad2deg(theta3));
solution = [Theta1,Theta2,Theta3];
fprintf("Calculated solution for IK is(are):\n")
disp(solution);