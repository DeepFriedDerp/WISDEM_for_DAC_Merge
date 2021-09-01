import os
import unittest

from wisdem.glue_code.runWISDEM import run_wisdem

test_dir = (
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    + os.sep
    + "examples"
    + os.sep
    + "02_reference_turbines"
    + os.sep
)
fname_modeling_options = test_dir + "modeling_options.yaml"
fname_analysis_options = test_dir + "analysis_options.yaml"


class TestRegression(unittest.TestCase):
    def test5MW(self):

        ## NREL 5MW
        fname_wt_input = test_dir + "nrel5mw.yaml"

        wt_opt, modeling_options, opt_options = run_wisdem(
            fname_wt_input, fname_modeling_options, fname_analysis_options
        )

        self.assertAlmostEqual(wt_opt["rotorse.re.precomp.blade_mass"][0], 16403.682326940743, 2)
        self.assertAlmostEqual(wt_opt["rotorse.rp.AEP"][0] * 1.0e-6, 23.8730557495, 2)
        self.assertAlmostEqual(wt_opt["financese.lcoe"][0] * 1.0e3, 51.6834637453, 2)
        self.assertAlmostEqual(wt_opt["rotorse.rs.tip_pos.tip_deflection"][0], 4.7673298062, 1)
        self.assertAlmostEqual(wt_opt["towerse.z_param"][-1], 87.7, 2)

    def test15MW(self):
        ## IEA 15MW
        fname_wt_input = test_dir + "IEA-15-240-RWT.yaml"
        wt_opt, modeling_options, opt_options = run_wisdem(
            fname_wt_input, fname_modeling_options, fname_analysis_options
        )

        self.assertAlmostEqual(wt_opt["rotorse.re.precomp.blade_mass"][0], 69911.6542917299, 1)
        self.assertAlmostEqual(wt_opt["rotorse.rp.AEP"][0] * 1.0e-6, 77.9923500907, 1)
        self.assertAlmostEqual(wt_opt["financese.lcoe"][0] * 1.0e3, 82.61519913199491, 1)
        self.assertAlmostEqual(wt_opt["rotorse.rs.tip_pos.tip_deflection"][0], 25.9593637967, 1)
        self.assertAlmostEqual(wt_opt["towerse.z_param"][-1], 144.386, 3)

    def test3p4MW(self):
        ## IEA 3.4MW
        fname_wt_input = test_dir + "IEA-3p4-130-RWT.yaml"
        wt_opt, modeling_options, opt_options = run_wisdem(
            fname_wt_input, fname_modeling_options, fname_analysis_options
        )

        self.assertAlmostEqual(wt_opt["rotorse.re.precomp.blade_mass"][0], 14555.7435212969, 1)
        self.assertAlmostEqual(wt_opt["rotorse.rp.AEP"][0] * 1.0e-6, 13.5747672872, 1)
        self.assertAlmostEqual(wt_opt["financese.lcoe"][0] * 1.0e3, 37.5717882723, 1)
        self.assertAlmostEqual(wt_opt["rotorse.rs.tip_pos.tip_deflection"][0], 7.3327691810, 1)
        self.assertAlmostEqual(wt_opt["towerse.z_param"][-1], 108.0, 3)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegression))
    return suite


if __name__ == "__main__":
    result = unittest.TextTestRunner().run(suite())

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
