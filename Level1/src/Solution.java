import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static int[] solution(int area) {
        // Your code here
        int[] result = new int[area + 1];
        int index = 0;
        int currentNum = (int) Math.floor(Math.sqrt(area));

        while(area > 0){

            int square = currentNum * currentNum;
            if(square <= area){

                result[index++] = square;
                area -= square;
            }
            currentNum = (int) Math.floor(Math.sqrt(area));
        }

        int[] final_result = new int[index];
        for(int i = 0; i<index;i++){

            final_result[i] = result[i];
        }

        for (int item:final_result){
            System.out.println(item);

        }
        System.out.println(final_result.length);

        return final_result;
    }

    public static void main(String[] args) {
        Solution.solution(15324);
    }
}