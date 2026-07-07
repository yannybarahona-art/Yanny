from source.credit_scorecard import evaluate_applicant

def test_evaluate_applicant():
    assert evaluate_applicant(
        85000,
        30000,
        "123456789"
        ) =={
            'dti_ratio':0.35,
            'tax_id':'XXX-XX-6789',
            'status':'Approved'
        }
    
