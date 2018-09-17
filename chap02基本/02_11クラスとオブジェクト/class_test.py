class Test:
    def show(self, val):
        print(self, val) # selfとvalを出力

test = Test()            # Testクラスをインスタンス化してオブジェクトの参照を代入
test.show('こんにちは')  # Testオブジェクトからshow()メソッドを実行
