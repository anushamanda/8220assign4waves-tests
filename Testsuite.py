from unittest import TestLoader, TestSuite, TextTestRunner
from UnitTest_customerregister import waves_Test1
from UnitTest_customerlogin import waves_Test2
from UnitTest_enrollevent import waves_Test3
from  UnitTest_enrolledevents import waves_Test4
from UnitTest_alreadyenrolled import waves_Test5
from UnitTest_logout import waves_Test6
from UnitTest_employeeregister import waves_Test7
from UnitTest_employeelogin import waves_Test8
from UnitTest_addevent import  waves_Test9
from UnitTest_updateevent import waves_Test10
from UnitTest_enrollmentlist import waves_Test11




if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(waves_Test1),
        loader.loadTestsFromTestCase(waves_Test2),
        loader.loadTestsFromTestCase(waves_Test3),
        loader.loadTestsFromTestCase(waves_Test4),
        loader.loadTestsFromTestCase(waves_Test5),
        loader.loadTestsFromTestCase(waves_Test6),
        loader.loadTestsFromTestCase(waves_Test7),
        loader.loadTestsFromTestCase(waves_Test8),
        loader.loadTestsFromTestCase(waves_Test9),
        loader.loadTestsFromTestCase(waves_Test10),
        loader.loadTestsFromTestCase(waves_Test11),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
