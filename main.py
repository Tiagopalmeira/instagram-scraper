import instaloader

# Solicita ao usuário o nome do perfil do Instagram e o número de likes para filtrar
nome = input("Digite o nome do perfil do Instagram para a raspagem: ")
num_likes = int(input("Quantos likes você gostaria de filtrar? "))

# Cria uma instância do Instaloader
loader = instaloader.Instaloader()

try:
    # Carrega o perfil do Instagram a partir do nome de usuário fornecido
    profile = instaloader.Profile.from_username(loader.context, nome)

    # Itera sobre as postagens do perfil
    for post in profile.get_posts():
        # Verifica se o número de likes da postagem é menor que o número especificado pelo usuário
        if post.likes < num_likes:
            # Imprime informações sobre a postagem
            print(f"Postagem: {post.url}, Likes: {post.likes}")

except instaloader.ProfileNotExistsException:
    print(f"O perfil '{nome}' não existe.")
except instaloader.RateLimitException:
    print("Excedeu o limite de requisições. Tente novamente mais tarde.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
