import statistics

def median(things):
    x = statistics.median(things)
    return x
    
def mode(things):
    y = statistics.mode(things)
    return y
    
def mean(things):
    z = statistics.mean(things)
    return z
    
def main():
    things = []
    
    for i in range(6):
        things.append(int(input('Enter a Value for the list: ')))
        
    print("List:", things)
    print("Median:", median(things))
    print("Mode:", mode(things))
    print("Mean:", mean(things))

if __name__ == "__main__":
    main()
    
