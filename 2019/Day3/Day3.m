clear
clc
load('Wires')

Path1 = GenerateData(Wire1);
Path2 = GenerateData(Wire2);
PathPoints1 = GeneratePoints(Path1);
PathPoints2 = GeneratePoints(Path2);
Crossing = [0, 0, 0, 0];

for i=1:length(PathPoints1)
    for j=1:length(PathPoints2)
        if PathPoints1(i,1) == PathPoints2(j,1) && PathPoints1(i,2) == PathPoints2(j,2)
            Crossing(end+1,:) = [PathPoints1(i,:), i, j];
        end
    end    
end

function Path = GenerateData(wire)
    Path = zeros(length(wire),2);
    Path(1,:) = [0, 0];
    for i=1:length(wire)
        tmp=char(wire(i));
        switch tmp(1)
            case 'R'
                Path(i+1,:) = [Path(i,1)+str2double(tmp(2:end)), Path(i,2)];
            case 'L'
                Path(i+1,:) = [Path(i,1)-str2double(tmp(2:end)), Path(i,2)];
            case 'U'
                Path(i+1,:) = [Path(i,1), Path(i,2)+str2double(tmp(2:end))];
            case 'D'
                Path(i+1,:) = [Path(i,1), Path(i,2)-str2double(tmp(2:end))];
            otherwise
                disp("Oops, not good")
                break;            
        end            
    end
    
end

function PathPoints = GeneratePoints(Path)
    PathPoints = [0,0];
    for i=1:length(Path)-1
        if Path(i,1) < Path(i+1,1)
            for j=Path(i,1)+1:Path(i+1,1)
                PathPoints(end+1,:) = [j, Path(i,2)];
            end
        elseif Path(i,1) > Path(i+1,1)
            for j=Path(i,1)-1:-1:Path(i+1,1)
                PathPoints(end+1,:) = [j, Path(i,2)];
            end
            
        elseif Path(i,2) < Path(i+1,2)
            for j=Path(i,2)+1:Path(i+1,2)
                PathPoints(end+1,:) = [Path(i,1), j];
            end
        elseif Path(i,2) > Path(i+1,2)
            for j=Path(i,2)-1:-1:Path(i+1,2)
                PathPoints(end+1,:) = [Path(i,1), j];
            end
        else
            disp("Not good")
            
        end        
        
    end

end