total = 0;

for i=153517:630395
    success = false;
    tmp=num2str(i);
    for j=1:5
       if str2num(tmp(j))>str2num(tmp(j+1))
           success = false;
           break;
       end
       if tmp(j) == tmp(j+1)
           if j>1 && j<5    
               if tmp(j-1)~= tmp(j) && tmp(j+2) ~= tmp(j)
                    success = true;
               end
           elseif j==1
               if tmp(j+2) ~= tmp(j)
                    success = true;
               end
           elseif j==5
               if tmp(j-1)~= tmp(j)
                    success = true;
               end
           end
       end
    end
    if success
        total = total + 1;
    end
end