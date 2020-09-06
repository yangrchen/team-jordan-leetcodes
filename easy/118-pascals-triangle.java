import java.util.Arrays;

/**
 * Pascal's Triangle.
 * 
 * Time: O(N^2), Space: O(N^2)
 * Relevant concepts: lists, arrays
 * 
 * Note that the file name being different from the class name is not acceptable at all
 * in Java. Java file names also cannot start with numbers. But that's okay. Only the
 * contents of this file need to be compilable.
 * 
 * @author Eric Schneider
 */
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<>();
        
        for(int i = 0; i < numRows; i++){
            if(i == 0)
                ret.add(Arrays.asList(1)); // Adds the initial [1]
            else{
                int lastIndex = ret.get(ret.size() - 1).size();
                Integer[] newVal = new Integer[lastIndex + 1];
                // Each row should start and end with 1.
                newVal[0] = 1; 
                newVal[lastIndex] = 1;
                
                // This fills the middle entries of the row with the summation of the two above it.
                for(int j = 1; j < lastIndex; j++)
                    newVal[j] = ret.get(ret.size() - 1).get(j - 1) + ret.get(ret.size() - 1).get(j);
                
                ret.add(Arrays.asList(newVal));
            }
        }
        
        return ret;
    }
}
