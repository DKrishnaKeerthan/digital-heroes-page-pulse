def analyze_security(response):

    headers = response.headers

    return {

        "https": response.url.startswith("https"),

        "strict_transport_security":
            "Strict-Transport-Security" in headers,

        "content_security_policy":
            "Content-Security-Policy" in headers,

        "x_frame_options":
            "X-Frame-Options" in headers,

        "x_content_type_options":
            "X-Content-Type-Options" in headers,

        "referrer_policy":
            "Referrer-Policy" in headers
    }