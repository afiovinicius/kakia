class TopicFilter:
    def __init__(self, topic):
        self.topic = topic.lower()

    def filter_content(self, response):
        content = []

        paragraphs = response.css("p::text").getall()
        headers = response.css("h1::text, h2::text, h3::text").getall()
        images = response.css("img")

        for paragraph in paragraphs:
            if self.topic in paragraph.lower():
                content.append({"type": "paragraph", "content": paragraph})

        for header in headers:
            if self.topic in header.lower():
                content.append({"type": "header", "content": header})

        for img in images:
            img_url = img.css("::attr(src)").get()
            alt_text = img.css("::attr(alt)").get()
            title_text = img.css("::attr(title)").get()
            if (alt_text and self.topic in alt_text.lower()) or (
                title_text and self.topic in title_text.lower()
            ):
                content.append(
                    {
                        "type": "image",
                        "src": img_url,
                        "alt": alt_text,
                        "title": title_text,
                    }
                )

        return content
