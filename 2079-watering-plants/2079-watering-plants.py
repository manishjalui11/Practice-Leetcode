class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        buck = capacity                      
        i = 0
        steps = 0
        while(i < len(plants)):
            steps += 1                     
            if(buck >= plants[i]):          
                buck-= plants[i]                  
            else:
                buck = capacity           
                buck-= plants[i]   
                steps += i+i             
            i += 1        
        return steps