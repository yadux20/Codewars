def calculate_years(principal, interest, tax, desired):
    yrs = 0
    current_p = principal
    
    while current_p < desired:
        yearly_interest = current_p * interest
        yearly_tax = yearly_interest * tax
        current_p += (yearly_interest - yearly_tax)
        yrs += 1
        
    return yrs