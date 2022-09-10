import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



def act_calculate(sex, )
# --------------------------------------------------------------------
# 一人当たりの必要摂取カロリー
# act = b * o * g [kcal]
# --------------------------------------------------------------------
        # 基礎代謝(B)の計算
            # 男性： 10×体重kg＋6.25×身長cmー5×年齢＋5
            # 女性： 10×体重kg+6.25×身長cm-5×年齢-16
        b = 0
        # 「活動量を入れた代謝量」を求めるために掛ける値
        oDict = {"one":1.2,"two":1.55,"three":1.725}
        # G(食事の目的)
        gDict ={"増量":1.2,"現状維持":1.0,"減量":0.8}
        # bo: b * o　のこと
        bo = 0

        if (sex == "男"):
            b = 10 * intWeight + 6.25 * intHeight - 5 * intAge + 5
            # boを計算する
            if (level == "one"):
                bo = b * oDict["one"]
            elif (level == "two"):
                bo = b * oDict["two"]
            elif (level == "three"):
                bo = b * oDict["three"]
            # actを計算する。
            if (activity == "増量"):
                act = bo * gDict["増量"]
            elif (activity == "現状維持"):
                act = bo * gDict["現状維持"]
            elif (activity == "減量"):
                act = bo * gDict["減量"]


        if (sex == "女"):
            b = 10 * intWeight + 6.25 * intHeight - 5 * intAge - 16
            # boを計算する
            if (level == "one"):
                bo = b * oDict["one"]
            elif (level == "two"):
                bo = b * oDict["two"]
            elif (level == "three"):
                bo = b * oDict["three"]
            # actを計算する。
            if (activity == "増量"):
                act = bo * gDict["増量"]
            elif (activity == "現状維持"):
                act = bo * gDict["現状維持"]
            elif (activity == "減量"):
                act = bo * gDict["減量"]