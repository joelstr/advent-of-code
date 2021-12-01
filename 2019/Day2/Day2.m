clear
clc
value = 0;

for x=0:99
   for y=0:99
       value = intcode(x,y);
       if value == 19690720
           display(["Noun is " x "Verb is " y "Result is " 100*x + y])
           break
       end
   end
   if value == 19690720
       break
   end
end

function output = intcode(noun,verb)
    load('input.mat')
    x=0;
    input(1+1) = noun;
    input(2+1) = verb;
    % input= [1,1,1,4,99,5,6,0,99];
    while input(x+1) ~= 99
        if input(x+1) == 1
            input(input(x+3+1)+1) = input(input(x+1+1)+1) + input(input(x+2+1)+1);
        elseif input(x+1) == 2
            input(input(x+3+1)+1) = input(input(x+1+1)+1) * input(input(x+2+1)+1);
        else
            display('Oops')
            break;
        end
        x = x+4;
    end
    output = input(1);
end