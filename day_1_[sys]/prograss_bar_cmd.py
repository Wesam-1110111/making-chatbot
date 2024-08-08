import sys



def progress_bar(progress, total):
    if len(sys.argv) >= 3:
        try:
            progress = float(sys.argv[1])
            total = int(sys.argv[2])
        except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)

    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f'\r|{bar}| {percent:.2f}%', end='\r')


n = [i for i in range(50000)]

progress_bar(0, len(n))
for i in n:
    x = i + i
    progress_bar(i+1, len(n))
print('\n')
