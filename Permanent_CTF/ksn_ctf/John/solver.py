import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

def main():
    pass_data = open("passwords", "r")
    user_pass_dic = {}

    for line in pass_data:
        pw, user = map(str, line.split())
        user_pass_dic[user] = pw

    logging.info(user_pass_dic)

    user_pass_dic = sorted(user_pass_dic.items())
    
    ans = ""
    for i in user_pass_dic:
        logging.info(i)
        ans += i[1][0]

    print(ans)

    
if __name__ == "__main__":
    main()
