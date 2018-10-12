# Contentful Content Containerization Demo
This demonstration project shows how a modern frontend framework may render content in different ways based upon the content type of the item.

The focus is the "Article" content type and demonstrates three different ways of rendering the same underlying model.

## Testing
- execute `docker run -d --name cfuldemo -p 8080:80 -e CONTENTFUL_API_TOKEN="<token-here>" -e SPACE_ID="<space-id-here>" cful`