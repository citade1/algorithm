// java code for the problem in https://school.programmers.co.kr/learn/courses/30/lessons/60057
import java.util.*;

class Solution{
    public int solution(String s) {
        int n = (int)s.length()/2;
        int[] lengthList = new int[n+1];

        for(int i=1;i<n+1;i++){
            String[] arr = strToChunk(s, i);
            String str = findPattern(arr);
            lengthList[i-1] = str.length();
        }
        lengthList[n] = s.length();
        
        int minLen = lengthList[0];
        for(int i=1;i<lengthList.length;i++){
            if(lengthList[i]<minLen)
                minLen = lengthList[i];
        }

        return minLen;
    }
    
    private String[] strToChunk(String str, int chunkSize){
        List<String> arr = new ArrayList<>();
    
        for(int i=0;i<str.length();i+=chunkSize){
            if(str.substring(i).length()<chunkSize){
                arr.add(str.substring(i));
            } else{
                arr.add(str.substring(i, i+chunkSize));
            }
        }
        
        return arr.toArray(new String[0]); 
    }
    
    private String findPattern(String[] arr){
        int count = 1;
        StringBuilder newStr = new StringBuilder();
    
        for(int i=1;i<arr.length;i++){
            if(arr[i].equals(arr[i-1])){
                count += 1;
                if(i==arr.length-1)
                    newStr.append(count).append(arr[i]); 
            }
            else{
                if(count>1){
                    newStr.append(count).append(arr[i-1]);
                }
                else{
                    newStr.append(arr[i-1]);
                }
                if(i==arr.length-1)
                    newStr.append(arr[i]);
                count = 1; //count 초기화
            }
        }
    
        return newStr.toString();
    }  
}

