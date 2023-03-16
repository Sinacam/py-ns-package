

def main():
    try:
        from libtest.foo import foo
        foo()
    except:
        print('No libtest.foo installed')

    try:
        from libtest.bar import bar
        bar()
    except:
        print('No libtest.bar installed')

    print('I am in main')


if __name__ == 'main':
    main()
