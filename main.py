from pyscript import document, display

def add_brand(e):
    document.getElementById('output1').innerHTML = ""
    brands = {'Uniqlo', 'Bench', 'Zara'}

    input_brand = document.getElementById('input1').value

    new_brand_set = {input_brand}

    all_brands = brands | new_brand_set # combines the two sets into one

    total_brands = len(brands | new_brand_set)

    brand_list = "<br>".join(sorted(all_brands))

    # display--
    document.getElementById('output1').innerHTML = f'All brands: <br> {brand_list}'
    display(f'Total Brands: {total_brands}', target="output1")