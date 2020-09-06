# Pascal's Triangle.
# 
# Time: O(N^2), Space: O(N^2)
# Relevant concepts: arrays
# 
# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    ret = []
    
    num_rows.times do |i|
        if i == 0 # Integer#times starts at 0
            ret << [1]
        else
            newRow = Array.new(i + 1)
            newRow[0] = 1;
            newRow[i] = 1;
            
            lastIndexOfLastRow = ret.last.length - 1
            
            (1..lastIndexOfLastRow).each do |j|
                newRow[j] = ret.last[j - 1] + ret.last[j]
            end
            
            ret << newRow
        end
    end
    
    ret
end
