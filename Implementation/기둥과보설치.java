// 문제: https://school.programmers.co.kr/learn/courses/30/lessons/60061?language=java

// 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있습니다.
// 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
// 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다. 단, 바닥은 벽면의 맨 아래 지면을 말합니다.
// 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기입니다. 맨 처음 벽면은 비어있는 상태입니다. 
// 기둥과 보는 격자선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있습니다. 다음은 기둥과 보를 설치해 구조물을 만든 예시입니다.

// 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때, 
// 모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

// n은 5 이상 100 이하인 자연수입니다.
// build_frame의 세로(행) 길이는 1 이상 1,000 이하입니다.
// build_frame의 가로(열) 길이는 4입니다.
// build_frame의 원소는 [x, y, a, b]형태입니다.
// x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
// a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
// b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
// 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
// 바닥에 보를 설치 하는 경우는 없습니다.
// 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
// 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
// 최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.
// return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
// return 하는 배열의 원소는 [x, y, a] 형식입니다.
// x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
// 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
// a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
// return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
// x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
// 입출력 예
// n	build_frame	                                                                                              result
// 5	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
// 5	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
// 주의!!! x 와 y를 바꿔 생각하지 말것. x,y는 2차원 좌표평면에서의 x,y와 동일!!! 

import java.util.*;

public class Main{ // for demonstration only
    public static void main(String[] args){
        int n = 5;
        int[][] build_frame = {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0},{2,2,0,1}};
        //int[][] build_frame = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
        Solution p = new Solution();
        int[][] result = p.solution(n, build_frame); 
        
        for(int i=0;i<result.length;i++){
            for(int j=0;j<result[i].length;j++){
                System.out.print(result[i][j]+" ");
            }
            System.out.println();
        }

    }
}

class Solution{

    public int[][] solution(int n, int[][] build_frame){
        
        boolean[][] pillars = new boolean[n+3][n+3];
        boolean[][] beams = new boolean[n+3][n+3];

        for(int[] cur: build_frame){
            int x = cur[0]+1;
            int y = cur[1]+1;
            int a = cur[2];
            int b = cur[3];

            if(b==0){
                delete(pillars, beams, x, y, a);
            } else{
                create(pillars, beams, x, y, a);
            } 
        }

        List<int[]> list = new ArrayList<>();
        for(int i=1;i<=n+1;i++){
            for(int j=1;j<=n+1;j++){
                if(pillars[i][j]==true){
                    list.add(new int[]{i-1,j-1,0});
                }
                if(beams[i][j]==true){
                    list.add(new int[]{i-1,j-1,1});
                }
            }
        }

        int[][] answer = new int[list.size()][3];
        for(int i=0;i<answer.length;i++){
            answer[i][0] = list.get(i)[0];
            answer[i][1] = list.get(i)[1];
            answer[i][2] = list.get(i)[2]; 
        }
        return answer;
    }

    private void create(boolean[][] pillars, boolean[][] beams, int x, int y, int a){
        if(a==0){ // 기둥 설치
            if(canPillars(pillars, beams, x, y)){
                pillars[x][y] = true;
            }
        } else{ // 보 설치
            if(canBeams(pillars, beams, x, y)){
                beams[x][y] = true;
            }
        }
    }
    private void delete(boolean[][] pillars, boolean[][] beams, int x, int y, int a){
        if(a==0){ // 기둥 삭제
            pillars[x][y] = false;
        } else{ // 보 삭제 
            beams[x][y] = false;
        }
        if(!canDelete(pillars, beams, pillars.length-3)){
            if(a==0){
                pillars[x][y] = true;
            } else{
                beams[x][y] = true;
            }
        }
    }
    private boolean canPillars(boolean[][] pillars, boolean[][] beams, int x, int y){
        if(y==1)
            return true;
        else if(pillars[x][y-1]==true)
            return true;
        else if(beams[x][y]==true || beams[x-1][y]==true)
            return true;
        
        return false;
    }
    private boolean canBeams(boolean[][] pillars, boolean[][] beams, int x, int y){
        if(pillars[x][y-1]==true || pillars[x+1][y-1]==true){
            return true;
        } else if(beams[x-1][y]==true && beams[x+1][y]==true){
            return true;
        }
        return false;
    }
    private boolean canDelete(boolean[][] pillars, boolean[][] beams, int n){
        for(int i=1;i<=n+1;i++){
            for(int j=1;j<=n+1;j++){
                if(pillars[i][j]==true & !(canPillars(pillars, beams, i, j))){
                    return false;
                }
                if(beams[i][j]==true & !(canBeams(pillars, beams, i, j))){
                    return false;
                }
            }
        }

        return true;
    }
}
