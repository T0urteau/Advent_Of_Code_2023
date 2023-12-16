import re
with open('aoc09_input.txt') as f:
    f = [[int(v) for v in val.split(" ")] for val in f.read().rstrip().split("\n")]
    
    def part1():
        ans = 0
        for n in range(len(f)):
            seq = [f[n]]
            seq_end = [f[n][-1]]

            step = 0
            diff = True

            while diff:
                old_tmp = 0
                tmp = 0
                diff = False
                new_seq = []

                for i in range(len(seq[step])-1):
                    tmp = seq[step][i+1] - seq[step][i]
                    new_seq.append(tmp)  
                    if i > 0 and tmp != old_tmp:
                        diff = True
                    old_tmp = tmp
                        
                seq_end.append(tmp)
                seq.append(new_seq)
                step += 1

            print(seq_end)
            ans += sum(seq_end)
        return(ans)
    
    def part2():
        ans = 0
        for n in range(len(f)):
            seq = [f[n][::-1]]
            seq_end = [f[n][0]]

            step = 0
            diff = True

            while diff:
                old_tmp = 0
                tmp = 0
                diff = False
                new_seq = []

                for i in range(len(seq[step])-1):
                    tmp = seq[step][i+1] - seq[step][i]
                    new_seq.append(tmp)  
                    if i > 0 and tmp != old_tmp:
                        diff = True
                    old_tmp = tmp
                        
                seq_end.append(tmp)
                seq.append(new_seq)
                step += 1

            print(seq_end)
            ans += sum(seq_end)
        return(ans)
    
    print(part1())
    print(part2())
    

    




    

    



    



    