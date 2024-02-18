%% Forward Kinematics using Homogeneous Matrix 
%% R configuration
clear all;clc;
display('R configuration...');
syms a0 the0

H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H = H01;

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])
l0 = 2; %2 units lenght 
t1 = 45; % 45 degrees
px=vpa(subs(H01(1,4),[the0,a0],[t1,l0]))
py=vpa(subs(H01(2,4),[the0,a0],[t1,l0]))
pz=vpa(subs(H01(3,4),[the0,a0],[t1,l0]))
%% R || R 
syms a0 a1 the0 the1;
display('R || R configuration...');
a0 = 2; %2 units lenght
a1 = 2;
H01 = [cosd(the0) -sind(the0) 0 a0*cosd(the0);...
      sind(the0)  cosd(the0) 0 a0*sind(the0);...
      0         0      1    0;...
      0         0      0    1];

H12= [cosd(the1) -sind(the1) 0 a1*cosd(the1);...
      sind(the1)  cosd(the1) 0 a1*sind(the1);...
      0         0      1    0;...
      0         0      0    1];

H = simplify(H01*H12);

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])

t1 = 45; % 45 degrees
t2 = 30;
px=vpa(subs(H(1,4),[the0,the1],[t1,t2]))
py=vpa(subs(H(2,4),[the0,the1],[t1,t2]))
pz=vpa(subs(H(3,4),[the0,the1],[t1,t2]))

%% R || R || R
clear all; clc;
display('R || R || R configuration...');
syms a0 a1 a2 the0 the1 the2;
a0 = 2; %2 units lenght
a1 = 2;
a2 = 2;

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

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])

t1 = 45; % 45 degrees
t2 = 30;
t3 = -45;
px=vpa(subs(H(1,4),[the0,the1,the2],[t1,t2,t3]))
py=vpa(subs(H(2,4),[the0,the1,the2],[t1,t2,t3]))
pz=vpa(subs(H(3,4),[the0,the1,the2],[t1,t2,t3]))

%% R _|_ R 
clear all; clc;
display('R _|_ R configuration...');
syms a0 a1 the0 the1;
a0 = 2; %2 units lenght
a1 = 2;
H01 = [cosd(the0)    0    sind(the0)   0;...
       sind(the0)    0   -cosd(the0)  0;...
       0            1       0       a0;...
       0            0       0       1];

H12= [cosd(the1) -sind(the1) 0 a1*cosd(the1);...
      sind(the1)  cosd(the1) 0 a1*sind(the1);...
      0         0      1    0;...
      0         0      0    1];

H = simplify(H01*H12);

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])

t1 = 0; % no base momemts
t2 = 30;
px=vpa(subs(H(1,4),[the0,the1],[t1,t2]))
py=vpa(subs(H(2,4),[the0,the1],[t1,t2]))
pz=vpa(subs(H(3,4),[the0,the1],[t1,t2]))

%% R _|_ R || R
clear all; clc;
disp("R _|_ R || R configuration, similar to clifford doc's ilustration.");
syms a0 a1 the0 the1 the2;
a0 = 2; %2 units lenght
a1 = 2;
H01 = [cosd(the0)    0    sind(the0)   0;...
       sind(the0)    0   -cosd(the0)  0;...
       0            1       0       0;...
       0            0       0       1];

H12= [cosd(the1) -sind(the1) 0 a0*cosd(the1);...
      sind(the1)  cosd(the1) 0 a0*sind(the1);...
      0         0      1    0;...
      0         0      0    1];

H23= [cosd(the2) -sind(the2) 0 a1*cosd(the2);...
      sind(the2)  cosd(the2) 0 a1*sind(the2);...
      0         0      1    0;...
      0         0      0    1];


H = simplify(H01*H12*H23);

% Computing the EE's Px, Py & Pz(essentially H[1:3,4])

t1 = 0; % no base momemts
t2 = 45;
t3 = 30;

px=vpa(subs(H(1,4),[the0,the1,the2],[t1,t2,t3]));
py=vpa(subs(H(2,4),[the0,the1, the2],[t1,t2,t3]));
pz=vpa(subs(H(3,4),[the0,the1,the2],[t1,t2,t3]));

disp(px);
disp(py);
disp(pz);
