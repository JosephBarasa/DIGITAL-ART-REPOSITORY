from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required
from Artworks.models import Artwork


def artist_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email format!')
            return redirect('artist_sign_up')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('artist_sign_up')
        
        # Check if username exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken!')
            return redirect('artist_sign_up')
        
        # Check if email exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('artist_sign_up')
        
        # Create and save artist
        user = CustomUser.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            role='artist',
        )
        user.save()
        
        messages.success(request, 'Your artist account has been created successfully!')
        return redirect('artist_sign_in')
        
    else:
        return render(request, 'artists/artist_sign_up.html')


def artist_sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'artist':
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('artist_index')
            else:
                messages.error(request, 'You are not registered as an artist.')
                return redirect('artist_sign_in')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('artist_sign_in')
        
    return render(request, 'artists/artists_sign_in.html')


def artist_index(request):
    return render(request, 'artists/artist_index.html')


@login_required
def artist_dashboard(request):
    artworks = Artwork.objects.filter(artist=request.user)
    return render(request, 'artists/artists_dashboard.html', {
        'user': request.user,
        'artworks': artworks,
    })



@login_required
def artist_profile_edit(request):
    user = request.user
    if request.method == 'POST':
        # Update fields from the form data
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.residence = request.POST.get('residence', user.residence)
        user.bio = request.POST.get('bio', user.bio)
        
        # Handle file upload for profile picture if provided
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        
        # Save updated user object
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('artist_dashboard')
    else:
        return render(request, 'artists/artist_profile_edit.html', {'user': user})


@login_required
def artwork_upload(request):  
    if request.method == 'POST':
        title = request.POST['title']
        media = request.POST['media']
        year = request.POST['year']
        price = request.POST['price']
        description = request.POST.get('description', '')
        
        artwork_image = request.FILES.get('artwork_image', None)
        
        # Create the artwork
        artwork = Artwork.objects.create(
            title=title,
            media=media,
            year=year,
            price=price,
            description=description,
            artwork_image=artwork_image,
            artist=request.user
        )

        messages.success(request, 'Your artwork has been successfully uploaded')
        return redirect('artist_dashboard') 

    return render(request, 'artists/artwork_upload.html')


# artwork edit

@login_required
def artwork_edit(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id, artist=request.user)
    
    if request.method == 'POST':
        artwork.title = request.POST.get('title', artwork.title)
        artwork.media = request.POST.get('media', artwork.media)
        artwork.year = request.POST.get('year', artwork.year)
        artwork.price = request.POST.get('price', artwork.price)
        artwork.description = request.POST.get('description', artwork.description)
        
        if 'artwork_image' in request.FILES:
            artwork.artwork_image = request.FILES['artwork_image']
            
        artwork.save()
        messages.success(request, 'Artwork updated successfully.')
        return redirect('artist_dashboard')
    
    return render(request, 'artists/artwork_edit.html', {'artwork': artwork})


# artwork deletion


def artwork_delete(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id, artist=request.user)

    if request.method == 'POST':
        artwork.delete()
        messages.success(request, 'Artwork deleted successfully.')
        return redirect('artist_dashboard')
    else:
        return render(request, 'artists/artwork_confirm_delete.html', {'artwork': artwork})


def artist_sign_out(request):
    logout(request)
    return redirect('home_index')


def artist_artists(request):
    artists = CustomUser.objects.filter(role='artist')
    return render(request, 'artists/artist_artists.html', {'artists': artists})


def artist_galleries(request):
    return render(request, 'artists/artist_gallery.html')


def artist_artworks(request):
    return render(request, 'artists/artist_artworks.html')


def artist_events(request):
    return render(request, 'artists/artist_events.html')


def artist_about(request):
    return render(request, 'artists/artist_about.html')


def artist_contact(request):
    return render(request, 'artists/artist_contact.html')


def artist_profile_display(request, artist_id):
    artist = get_object_or_404(CustomUser, id=artist_id, role='artist')
    artworks = Artwork.objects.filter(artist=artist)
    return render(request, 'artists/artist_profile_display.html',
                  {'artist': artist, 'artworks': artworks })
    
    

