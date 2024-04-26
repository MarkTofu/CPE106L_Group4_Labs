import statistics

def median(things):
    if not things:
        return 0
    else:
        x = statistics.median(things)
        return x
    
def mode(things):
    if not things:
        return 0
    else:
        y = statistics.mode(things)
        return y
    
def mean(things):
    if not things:
        return 0
    else:
        z = statistics.mean(things)
        return z
    
def main():
    things = []
        
    print("Median:", median(things))
    print("Mode:", mode(things))
    print("Mean:", mean(things))

if __name__ == "__main__":
    main()

