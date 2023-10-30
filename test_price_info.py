import price_info as cost

def test_total_cost_of_shopping():
    test_cost=46.75
    test_result=cost.total_cost_shopping()
    assert (test_result==test_cost)

def test_cost_of_fruits():
    test_fruit='orange'
    test_quantity=7
    test_cost=9.8
    test_result=round(cost.cost_of_fruits(test_fruit,test_quantity),2)
    assert (test_result==test_cost)
