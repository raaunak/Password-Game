from project import rule_5, rule_6, rule_7, rule_10
import datetime

def main():
    test_rule_5()
    test_rule_6()

def test_rule_5():
    assert rule_5("5555") == True
    assert rule_5("44444") == True
    assert rule_5("2155") == False

def test_rule_6():
    todays_date = datetime.datetime.now()
    todays_month = todays_date.strftime('%B')
    assert rule_6(todays_month) == True
    assert rule_6("hllo") == False

def test_rule_7():
    assert rule_7("ronaldo") == True
    assert rule_7("messi") == False
    assert rule_7("bale") == True
    assert rule_7("neymar") == True
    assert rule_7("salah") == True

def test_rule_10():
    assert rule_10("12345") == True
    assert rule_10("1234") == False
    assert rule_10("1234567") == True


if __name__ == "__main__":
    main()
