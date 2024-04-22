"""
This file for longest substring search algorithm
"""

class Competition():
    def __init__(self, text_1:str, text_2:str):
        self.text_1 = text_1
        self.text_2 = text_2
        
    def tonkaow_algorithm(self):
        """
        Algorithm from tonkaow
        """
        import numpy as np

        # first we need to check if text1 and text2 exist at the first place?
        if len(self.text_1) == 0 or len(self.text_2) == 0:
                print("ใส่คำก่อนไหมแม่ งง")
                return(-1,-1,0)
        # Then we need to check if text1 and text2 contain same character whatsoever?
        elif len(set(self.text_1).intersection(set(self.text_2))) == 0:
                print("ไม่ต้องหาหรอกจ้ามันไม่มี")
                return(-1,-1,0)
        # Then we need to check if text1 and text 2 is the same text or not?
        elif self.text_1 == self.text_2:
                print(f"The longest substring is {self.text_1} and the length is {len(self.text_1)} starting from index 0")
                return(0,0,len(self.text_1))
        # We will use matrix to approch our solution
        This_matrix = np.zeros(shape=(len(self.text_2),len(self.text_1)),dtype=np.int8)                             #We generate len(text2)*len(text1) 0 matrix. Later on we will change the value in this matrix
        for ri in range(len(self.text_2)):                                                                          #We start from row then to column
            for ci in range(len(self.text_1)):  
                if self.text_2[ri] == self.text_1[ci]:
                    if ri == 0 or ci == 0:
                        This_matrix[ri][ci]=1
                    elif This_matrix[ri-1][ci-1]>0:
                        This_matrix[ri][ci]=This_matrix[ri-1][ci-1]+1
                    else:
                        This_matrix[ri][ci]=1
        max_length_index = np.unravel_index(np.argmax(This_matrix),This_matrix.shape)
        max_length = This_matrix[max_length_index[0]][max_length_index[1]]
        start_text2_index = max_length_index[0]-(max_length-1)
        start_text1_index = max_length_index[1]-(max_length-1)
        print(This_matrix)
        print(start_text1_index,start_text2_index,max_length)
        return(start_text1_index,start_text2_index,max_length)