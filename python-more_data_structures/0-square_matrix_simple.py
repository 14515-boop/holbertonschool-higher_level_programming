#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []  # Orijinala toxunmamaq üçün yeni boş matris yaradırıq
    
    for row in matrix:
        new_row = []  # Hər sətir üçün yeni boş sətir yaradırıq
        for x in row:
            new_row.append(x ** 2)  # Elementin kvadratını yeni sətirə əlavə edirik
        new_matrix.append(new_row)  # Hazır olan sətiri yeni matrisə əlavə edirik
        
    return new_matrix
