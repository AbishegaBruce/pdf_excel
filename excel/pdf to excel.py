import tabula
inp=(r"table.pdf")
oup=(r"test.csv")
df=tabula.read_pdf(input_path=inp,pages="1")
tabula.convert_into(input_path=inp,output_path=oup,output_format="csv",pages="1",stream=True)