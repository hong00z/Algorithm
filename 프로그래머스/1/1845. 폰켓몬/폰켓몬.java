import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(Integer num : nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        int counter = map.size();
        if (n/2 > counter) {
            answer = counter;
        }
        else {
            answer = n/2;
        }
        return answer;
    }
}