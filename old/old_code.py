# picture.tags.append(top_tag)
# Store the corresponding tag for each emoji
# tag_votes[picture.image_url][emojis_tags[i]] = top_tag
# print(tag_votes[picture.image_url][emojis_tags[i]])
# tagged_images[picture.image_url].append(top_tag.lower())
# print(picture.to_json())
# print(picture.to_json())

'''
@bot.command()
async def tag(ctx, *tags):
    if ctx.message.attachments:
        image_url = ctx.message.attachments[0].url
        if image_url in tagged_images:
            for tag in tags:
                tag_votes[image_url][ctx.message.author.id] = tag
                await ctx.send(f'Tag \'{tag}\' added for the image.')
        else:
            await ctx.send('This image was not fetched by the bot.')
'''
# print(reaction)
# print(reaction.emoji)
# print(reaction.message.id)

# print(len(message.embeds))
# print(message.embeds[0])
# print(message.embeds[0].url)
# print(message.embeds[0].author)
# print(message.embeds[0].image.url)

# print(reaction.messsage.id, reaction.emoji)

'''
@bot.command()
async def search_tags(ctx, *tags):
    matched_images = []
    for image_url, image_tags in tagged_images.items():
        if all(tag.lower() in image_tags for tag in tags):
            matched_images.append(image_url)

    if matched_images:
        await ctx.send("Matching images:")
        for image_url in matched_images:
            await ctx.send(image_url)
    else:
        await ctx.send("No images found matching the provided tags.")
'''
'''
@bot.event
async def on_raw_reaction_add(payload): #reaction, user):
    # Check if the reaction is added to a message suggested by the bot
    user = payload.member
    print(user)
    print(payload)
    print(payload.emoji.name)
    # reaction = payload.reaction
'''

'''
@bot.command()
async def search(ctx, *tags):
    matched_images = []
    for image_url, image_tags in tagged_images.items():
        if all(tag.lower() in image_tags for tag in tags):
            matched_images.append(image_url)
    
    if matched_images:
        await ctx.send('Matching images:')
        for image_url in matched_images:
            await ctx.send(image_url)
    else:
        await ctx.send('No images found matching the provided tags.')

@bot.command()
async def random_untagged(ctx):
    untagged_images = [image_url for image_url, tags in tagged_images.items() if not tags]
    if untagged_images:
        random_image = random.choice(untagged_images)
        await ctx.send(f'Here\'s a random untagged image: {random_image}')
        await ctx.send('Please tag this image using \'!tag <tags>\'.')
    else:
        await ctx.send('No untagged images found.')
'''
# tagged_images[image_url] = []
# tag_votes[image_url] = {}