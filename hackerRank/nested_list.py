if __name__ == '__main__':
        
    name = ['Betty', 'Armando', 'Patricia']
    score = [10.3, 20.5, 30.2]
    
    sorted_score = sorted(score)
    records = sorted(list(zip(name, score)))


    for name, score in records:
        if score == sorted_score[-2]:
            print(name)

    