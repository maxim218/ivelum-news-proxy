def is_header_allowed(header):
    prohibited_headers = ["CONNECTION", "CONTENT-LENGTH", "TRANSFER-ENCODING"]
    header_in_array_flag = (header.upper() in prohibited_headers)
    return (header_in_array_flag == False)
