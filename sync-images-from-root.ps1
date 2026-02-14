# Sync ALL images from ROOT (every folder and subfolder) into website/assets
# Run from: d:\Workspace\website
# Also: Me images/output, mastermind/assets

$websiteAssets = "d:\Workspace\website\assets"
$rootBase = "d:\Workspace\ROOT"
$meOutput = "d:\Workspace\Me images\output"
$mastermindAssets = "d:\Workspace\mastermind\assets"

# Folder mapping: ROOT/images/X -> assets/Y
$rootFolders = @{
    "images\david-tech" = "david"
    "images\products" = "products"
    "images\platform" = "platform"
    "images\marketing" = "marketing"
}

# Ensure base subfolders exist
@("david", "products", "platform", "marketing", "root", "embellishments", "modules") | ForEach-Object {
    $p = Join-Path $websiteAssets $_
    if (!(Test-Path $p)) { New-Item -ItemType Directory -Path $p -Force | Out-Null }
}

# Exclude images not used on site (reduces load)
$syncExclude = @('mastermind-launch-announcement', 'mastermind-banner-installable')

# Recursively copy ALL images from entire ROOT tree
$extensions = @("*.png", "*.jpg", "*.jpeg", "*.webp", "*.gif", "*.svg")
$count = 0
Get-ChildItem $rootBase -Recurse -File | Where-Object { $_.Extension -match '\.(png|jpg|jpeg|webp|gif|svg)$' } | ForEach-Object {
    $rel = $_.FullName.Substring($rootBase.Length).TrimStart("\")
    $leaf = Split-Path $rel -Leaf
    $skip = $false
    foreach ($ex in $syncExclude) { if ($leaf -like "*$ex*") { $skip = $true; break } }
    if ($skip) { return }
    $matched = $false
    foreach ($map in $rootFolders.GetEnumerator()) {
        if ($rel.StartsWith($map.Key, [StringComparison]::OrdinalIgnoreCase)) {
            $subpath = $rel.Substring($map.Key.Length).TrimStart("\")
            $dstDir = Join-Path $websiteAssets $map.Value
            if ($subpath) {
                $subdir = Split-Path $subpath -Parent
                $dstDir = Join-Path $dstDir $subdir
            }
            if (!(Test-Path $dstDir)) { New-Item -ItemType Directory -Path $dstDir -Force | Out-Null }
            $dst = Join-Path $dstDir (Split-Path $rel -Leaf)
            Copy-Item $_.FullName $dst -Force
            Write-Host "  ROOT/$rel"
            $count++
            $matched = $true
            break
        }
    }
    if (-not $matched) {
        $dstDir = Join-Path $websiteAssets "root"
        $dstPath = Join-Path $dstDir $rel
        $dstParent = Split-Path $dstPath -Parent
        if (!(Test-Path $dstParent)) { New-Item -ItemType Directory -Path $dstParent -Force | Out-Null }
        Copy-Item $_.FullName $dstPath -Force
        Write-Host "  ROOT/$rel (-> root/)"
        $count++
    }
}

# Me images
if (Test-Path $meOutput) {
    Get-ChildItem $meOutput -Include *.png,*.jpg,*.jpeg,*.webp | ForEach-Object {
        $name = $_.Name
        $dest = $websiteAssets
        if ($name -match "^david-") { $dest = Join-Path $websiteAssets "david" }
        elseif ($name -match "hero-banner|social-card|embellishment") { $dest = Join-Path $websiteAssets "products" }
        elseif ($name -match "cta-|badge-|newsletter-|blog-|contact-|about-|video-") { $dest = Join-Path $websiteAssets "marketing" }
        Copy-Item $_.FullName (Join-Path $dest $name) -Force
        Write-Host "  Me: $name"
        $count++
    }
}

# Fallbacks: copy key phyllux-* from products to assets root (for onerror fallbacks)
$fallbacks = @(
    @{ from = 'phyllux-hero-banner-1920x600.png'; to = 'phyllux-hero-banner.png' },
    @{ from = 'phyllux-about-hero.png'; to = 'phyllux-about-hero.png' },
    @{ from = 'phyllux-embellishment.png'; to = 'phyllux-embellishment.png' },
    @{ from = 'phyllux-footer-divider.png'; to = 'phyllux-footer-divider.png' },
    @{ from = 'phyllux-engenica-hero.png'; to = 'phyllux-engenica-hero.png' },
    @{ from = 'phyllux-tech-hero.png'; to = 'phyllux-tech-hero.png' },
    @{ from = 'phyllux-proof-hero.png'; to = 'phyllux-proof-hero.png' },
    @{ from = 'phyllux-ethics-hero.png'; to = 'phyllux-ethics-hero.png' },
    @{ from = 'phyllux-docs-hero.png'; to = 'phyllux-docs-hero.png' }
)
foreach ($fb in $fallbacks) {
    $src = Join-Path (Join-Path $websiteAssets "products") $fb.from
    if (Test-Path $src) {
        Copy-Item $src (Join-Path $websiteAssets $fb.to) -Force
        Write-Host "  Fallback: $($fb.to)"
        $count++
    }
}

# MASTERMIND Results So Far (PDF) — copy from ROOT to website assets
$resultsPdf = Join-Path $rootBase "MASTERMIND_RESULTS_SO_FAR.pdf"
if (Test-Path $resultsPdf) {
    Copy-Item $resultsPdf (Join-Path $websiteAssets "MASTERMIND_RESULTS_SO_FAR.pdf") -Force
    Write-Host "  ROOT: MASTERMIND_RESULTS_SO_FAR.pdf"
    $count++
}

# Mastermind
if (Test-Path $mastermindAssets) {
    $modDest = Join-Path $websiteAssets "modules"
    Get-ChildItem $mastermindAssets -Include *.png,*.jpg,*.jpeg | ForEach-Object {
        Copy-Item $_.FullName (Join-Path $modDest $_.Name) -Force
        Write-Host "  MASTERMIND: $($_.Name)"
        $count++
    }
}

Write-Host "`nSync complete. $count images from ROOT (+ Me/MASTERMIND)." -ForegroundColor Cyan
Write-Host "Do NOT push to any repo without explicit approval." -ForegroundColor Yellow
