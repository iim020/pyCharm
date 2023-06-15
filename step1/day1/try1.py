# 예외 처리 try ~ except

def test (values):
    sum = None
    try:
        sum = values[0]+ values[1]+values[2]
    except IndexError as error:
        print(str(error))
    except Exception as err:
        print(err)
    else:
        print("정상처리")
    finally:
        print("무조건")

test([1,2])