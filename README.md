### Preference_selection

##### Give a list of products by filter out the dominated products based on the specificed directional preferences.
##### Input: 
a list of products (products), a list of perference (perferences) and the individual directional preference is represented as a pair (i,p)
where i referes to the index of feature of productsand p is 1 or -1 depending on whether the user wants the feature of product be positive or negative
##### Output: 
list of the products that are relevant
    
##### For example:
- phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Galaxy S21', 'Samsung', 6.2, 3300, 1348],['Nova 5T', 'Huawei', 6.26, 3700, 497],['P30 Pro', 'Huawei', 6.4, 3500, 398],['R17 Pro', 'Oppo', 6.6, 3200, 457],['Pixel 3', 'Google', 6.3, 3800, 688]]
- big_screen = [(2,1)]
- relevant(phones, big_screen)
[['R17 Pro', 'Oppo', 6.6, 3200, 457]]
- big_screen_but_cheap = [(2,1),(4,-1)]
- relevant(phones, big_screen_but_cheap)
[['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457]]
