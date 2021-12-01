clear
clc
value = 0;
SystemID = 5;

load('input.mat')
x=0;
while input(x+1) ~= 99
    tmp = ['0000' num2str(input(x+1))];
    if str2double(tmp(end-1:end)) == 1
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        input(input(x+3+1)+1) = param1 + param2;
        x = x+4;
    elseif str2double(tmp(end-1:end)) == 2
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        input(input(x+3+1)+1) = param1 * param2;
        x = x+4;
    elseif str2double(tmp(end-2:end)) == 3
        input(input(x+1+1)+1) = SystemID;
        x = x+2;
    elseif str2double(tmp(end-1:end)) == 4
        if str2double(tmp) > 100
            disp(input(x+1+1))
        else
            disp(input(input(x+1+1)+1))
        end
        x = x+2;
    elseif str2double(tmp(end-1:end)) == 5
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        if param1 ~= 0
            x = param2;
        else
            x = x+3;
        end

    elseif str2double(tmp(end-1:end)) == 6
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        if param1 ~= 0
            x = x+3;
        else
            x = param2;
        end

    elseif str2double(tmp(end-1:end)) == 7
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        
        if param1 < param2
           input(input(x+3+1)+1) = 1;
        else
            input(input(x+3+1)+1) = 0;
        end
        x = x + 4;
        
    elseif str2double(tmp(end-1:end)) == 8
        if str2double(tmp(end-2)) == 1
            param1 = input(x+1+1);
        else
            param1 = input(input(x+1+1)+1);
        end
        if str2double(tmp(end-3)) == 1
            param2 = input(x+2+1);
        else
            param2 = input(input(x+2+1)+1);
        end
        
        if param1 == param2
           input(input(x+3+1)+1) = 1;
        else
            input(input(x+3+1)+1) = 0;
        end
        x = x + 4;
        
        
    else
        disp('Oops')
        break;
    end
end