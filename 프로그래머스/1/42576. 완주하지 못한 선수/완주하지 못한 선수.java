
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();
        for (String name : participant) {
	          map.put(name, map.getOrDefault(name, 0)+1);
				}
				for (String name : completion) {
	          map.put(name, map.get(name)-1);
				}
				
				for (String key : map.keySet()) {
					  if (map.get(key) > 0) {
							  answer = key;
							  break;
						}
				}
        return answer;
    }
}

/* HashMap.getOrDefault(Object key, Object defaultValue)*/
// 1) Java 8에 추가된 Collection API 메서드
// 2) 찾는 key가 존재하면 key의 value를 반환하고, 없을 경우(null) defaultValue를 반환