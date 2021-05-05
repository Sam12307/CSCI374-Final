def test_minus_one(self):
    t= AssemblyTest(self, "abs.s")
    t.input_scalar("a0", -1)
    t.call("abs")
    t.check_scalar("a0", 1)
    t.execute()

