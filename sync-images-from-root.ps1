# Sync images from ROOT and Me images into website/assets
# Run from: d:\Workspace\website
# Sources: D:\Workspace\ROOT\images, D:\Workspace\Me images\output

$websiteAssets = "d:\Workspace\website\assets"
$rootImages = "d:\Workspace\ROOT\images"
$meOutput = "d:\Workspace\Me images\output"
$mastermindAssets = "d:\Workspace\mastermind\assets"

# Create subfolders
$subfolders = @("david", "products", "platform", "marketing", "embellishments", "modules")
foreach ($sub in $subfolders) {
    $path = Join-Path $websiteAssets $sub
    if (!(Test-Path $path)) { New-Item -ItemType Directory -Path $path -Force | Out-Null }
}

# Copy from ROOT/images (recursive). Map subfolders to assets/
# ROOT/images: david-tech, products, platform, marketing (embellishments live in products/marketing)
$rootFolders = @{
    "david-tech" = "david"
    "products" = "products"
    "platform" = "platform"
    "marketing" = "marketing"
}
if (Test-Path $rootImages) {
    foreach ($sub in $rootFolders.Keys) {
        $src = Join-Path $rootImages $sub
        $dst = Join-Path $websiteAssets $rootFolders[$sub]
        if (Test-Path $src) {
            if (!(Test-Path $dst)) { New-Item -ItemType Directory -Path $dst -Force | Out-Null }
            Get-ChildItem $src -Include *.png,*.jpg,*.jpeg,*.webp,*.gif,*.svg | ForEach-Object {
                Copy-Item $_.FullName (Join-Path $dst $_.Name) -Force
                Write-Host "  ROOT/$sub : $($_.Name)"
            }
        }
    }
    # Root-level images
    Get-ChildItem $rootImages -File -Include *.png,*.jpg,*.jpeg,*.webp,*.gif,*.svg | ForEach-Object {
        Copy-Item $_.FullName (Join-Path $websiteAssets $_.Name) -Force
        Write-Host "  ROOT: $($_.Name)"
    }
}

# Copy from Me images/output (flatten to assets/david/ and assets/products/)
if (Test-Path $meOutput) {
    Get-ChildItem $meOutput -Include *.png,*.jpg,*.jpeg,*.webp | ForEach-Object {
        $name = $_.Name
        $dest = $websiteAssets
        if ($name -match "^david-") { $dest = Join-Path $websiteAssets "david" }
        elseif ($name -match "hero-banner|social-card|embellishment") { $dest = Join-Path $websiteAssets "products" }
        elseif ($name -match "cta-|badge-|newsletter-|blog-|contact-|about-|video-") { $dest = Join-Path $websiteAssets "marketing" }
        Copy-Item $_.FullName (Join-Path $dest $name) -Force
        Write-Host "  Me: $name"
    }
}

# Copy from mastermind/assets (module images)
if (Test-Path $mastermindAssets) {
    $modDest = Join-Path $websiteAssets "modules"
    Get-ChildItem $mastermindAssets -Include *.png,*.jpg,*.jpeg | ForEach-Object {
        Copy-Item $_.FullName (Join-Path $modDest $_.Name) -Force
        Write-Host "  MASTERMIND: $($_.Name)"
    }
}

Write-Host "`nSync complete. Run deploy-to-repo.ps1 to push." -ForegroundColor Cyan
