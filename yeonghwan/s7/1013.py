T = int(input())

def check(wave,result):
    while len(wave) > 0:

        if wave[:3] == "100":
            wave = wave[3:]
            
            while len(wave) > 0 and  wave[:1] == "0":
                wave = wave[1:]

            if len(wave) == 0:
                result = False
                break
            
            wave = wave[1:]

            while len(wave) > 0 and wave[:1] == "1":
                if len(wave) >= 3 and wave[:3] == "100":
                    break
                else:
                    wave = wave[1:]

        elif wave[:2] == "01":
            wave = wave[2:]

        else:
            result = False
            break
    
    return result

for _ in range(T):
    wave = str(input())
    result = True

    answer = "YES" if check(wave, result) else "NO"
    print(answer)