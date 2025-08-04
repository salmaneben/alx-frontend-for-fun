# SASS & SCSS

This module provides a comprehensive introduction to CSS preprocessing using SASS (Syntactically Awesome StyleSheets) and SCSS (Sassy CSS). It demonstrates progressive learning from basic concepts to advanced features, showing how to write more maintainable, organized, and powerful CSS.

## 🎯 Learning Objectives

- Understand the difference between SASS and SCSS syntax
- Master variables, mixins, and functions
- Implement control directives (loops, conditionals)
- Organize CSS with partials and imports
- Use advanced SASS features for efficient styling
- Compile SASS/SCSS to production-ready CSS

## 📁 Module Structure

```
sass_scss/
├── README.md                # This comprehensive documentation
├── 0-debug_log.scss        # Debug output and logging
├── 1-color_variable.scss   # Basic variable usage
├── 2-color_variables.scss  # Multiple variables
├── 3-nested_tag.scss       # Nested selectors
├── 4-nested_class.scss     # Nested classes
├── 5-nested_child.scss     # Child selectors
├── 6-nested_hover.scss     # Pseudo-class nesting
├── 7-nested_deeper.scss    # Deep nesting examples
├── 8-mixin_margins.scss    # Mixin implementation
├── 9-extend_list.scss      # Inheritance with @extend
├── 10-import_colors.scss   # Importing partials
├── 11-loop_photos.scss     # Loop through lists
├── 12-loop_header.scss     # Header styling with loops
├── 100-loop_col.scss       # Column grid with loops
├── 101-media_query.scss    # Media query mixins
└── 102-media_query.scss    # Advanced media queries
```

## 🚀 Progressive Learning Path

### Level 1: Fundamentals

#### 1. Debug Output (0-debug_log.scss)
```scss
// Basic debug functionality
@debug 'Hello world';
```
**Concept:** Using SASS debug statements for development

#### 2. Variables (1-color_variable.scss)
```scss
// Define and use variables
$text-color: #3D3D3D;

body {
  color: $text-color;
}

p {
  color: $text-color;
}
```
**Concept:** Variable definition and usage for maintainable code

#### 3. Multiple Variables (2-color_variables.scss)
```scss
// Multiple variable management
$primary-color: #FF6B35;
$secondary-color: #004E89;
$text-color: #3D3D3D;
$background-color: #F5F5F5;

.header {
  background-color: $primary-color;
  color: $text-color;
}
```
**Concept:** Color system management with variables

### Level 2: Nesting

#### 4. Tag Nesting (3-nested_tag.scss)
```scss
// Nested selectors for related elements
.navigation {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
    
    li {
      display: inline-block;
      
      a {
        text-decoration: none;
        color: $primary-color;
      }
    }
  }
}
```
**Concept:** Hierarchical CSS organization

#### 5. Class Nesting (4-nested_class.scss)
```scss
// Nested classes for component organization
.card {
  border: 1px solid #ddd;
  border-radius: 4px;
  
  .card-header {
    background-color: $background-color;
    padding: 1rem;
    
    .card-title {
      margin: 0;
      font-size: 1.25rem;
    }
  }
  
  .card-body {
    padding: 1rem;
  }
}
```
**Concept:** Component-based styling organization

#### 6. Child Selectors (5-nested_child.scss)
```scss
// Direct child selectors
.menu {
  > li {
    display: inline-block;
    
    > a {
      padding: 0.5rem 1rem;
      
      &:hover {
        background-color: $primary-color;
      }
    }
  }
}
```
**Concept:** Precise selector targeting

#### 7. Pseudo-classes (6-nested_hover.scss)
```scss
// Nested pseudo-classes and states
.button {
  background-color: $primary-color;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  
  &:hover {
    background-color: darken($primary-color, 10%);
  }
  
  &:active {
    background-color: darken($primary-color, 20%);
  }
  
  &:disabled {
    background-color: $secondary-color;
    opacity: 0.5;
  }
}
```
**Concept:** State management with parent selectors

### Level 3: Advanced Features

#### 8. Mixins (8-mixin_margins.scss)
```scss
// Reusable mixin definitions
@mixin marginLR($property) {
  margin-left: $property;
  margin-right: $property;
}

body {
  @include marginLR(10px);
}

div {
  @include marginLR(15px);
}
```
**Concept:** Code reusability with parameterized mixins

#### 9. Inheritance (9-extend_list.scss)
```scss
// Placeholder selectors and inheritance
%list-style {
  margin: 0;
  padding: 0;
  list-style: none;
}

.navigation-list {
  @extend %list-style;
  display: flex;
}

.sidebar-list {
  @extend %list-style;
  display: block;
}
```
**Concept:** DRY principle with placeholder selectors

### Level 4: Control Directives

#### 10. Loops (100-loop_col.scss)
```scss
// Generate grid columns with loops
@for $i from 1 through 4 {
  .col-#{$i} { 
    width: 100% / 4 * $i; 
  }
}
```
**Concept:** Dynamic CSS generation with loops

#### 11. List Iteration (11-loop_photos.scss)
```scss
// Loop through lists
$photo-names: 'photo1', 'photo2', 'photo3', 'photo4';

@each $photo in $photo-names {
  .photo-#{$photo} {
    background-image: url('images/#{$photo}.jpg');
  }
}
```
**Concept:** Dynamic content generation

### Level 5: Organization

#### 12. Imports (10-import_colors.scss)
```scss
// Importing external files
@import 'colors';
@import 'typography';
@import 'layout';

// Using imported variables
body {
  color: $text-color;
  font-family: $font-family-base;
}
```
**Concept:** Modular CSS architecture

#### 13. Media Queries (101-media_query.scss)
```scss
// Responsive design with mixins
@mixin mobile {
  @media screen and (max-width: 767px) {
    @content;
  }
}

@mixin tablet {
  @media screen and (min-width: 768px) and (max-width: 1023px) {
    @content;
  }
}

.container {
  width: 100%;
  max-width: 1200px;
  
  @include mobile {
    padding: 0 1rem;
  }
  
  @include tablet {
    padding: 0 2rem;
  }
}
```
**Concept:** Responsive design organization

## 🛠️ SASS/SCSS Features Demonstrated

### Variables
```scss
// Colors
$primary-color: #007bff;
$secondary-color: #6c757d;

// Typography
$font-family-base: 'Helvetica Neue', Arial, sans-serif;
$font-size-base: 1rem;
$line-height-base: 1.5;

// Spacing
$spacer: 1rem;
$spacers: (
  0: 0,
  1: $spacer * 0.25,
  2: $spacer * 0.5,
  3: $spacer,
  4: $spacer * 1.5,
  5: $spacer * 3
);
```

### Mixins
```scss
// Button mixin with parameters
@mixin button-variant($color, $background, $border) {
  color: $color;
  background-color: $background;
  border-color: $border;
  
  &:hover {
    color: $color;
    background-color: darken($background, 7.5%);
    border-color: darken($border, 10%);
  }
}

// Usage
.btn-primary {
  @include button-variant(white, $primary-color, $primary-color);
}
```

### Functions
```scss
// Custom functions
@function rem($pixels) {
  @return #{$pixels / 16}rem;
}

// Color manipulation
@function theme-color($key: "primary") {
  @return map-get($theme-colors, $key);
}

// Usage
.text {
  font-size: rem(18); // 1.125rem
  color: theme-color("primary");
}
```

### Control Directives
```scss
// Conditional statements
@mixin text-emphasis-variant($parent, $color) {
  #{$parent} {
    color: $color !important;
  }
  
  @if $emphasized-link-hover-darken-percentage != 0 {
    a#{$parent}:hover,
    a#{$parent}:focus {
      color: darken($color, $emphasized-link-hover-darken-percentage) !important;
    }
  }
}

// Loops with maps
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px
);

@each $breakpoint, $value in $grid-breakpoints {
  .container-#{$breakpoint} {
    max-width: $value;
  }
}
```

## 🎨 Advanced Patterns

### BEM with SASS
```scss
.block {
  &__element {
    color: $primary-color;
    
    &--modifier {
      font-weight: bold;
    }
  }
  
  &--block-modifier {
    background-color: $secondary-color;
  }
}
```

### Responsive Typography
```scss
@mixin responsive-font-size($min-size, $max-size, $min-screen: 320px, $max-screen: 1200px) {
  font-size: $min-size;
  
  @media screen and (min-width: $min-screen) {
    font-size: calc(#{$min-size} + #{strip-unit($max-size - $min-size)} * ((100vw - #{$min-screen}) / #{strip-unit($max-screen - $min-screen)}));
  }
  
  @media screen and (min-width: $max-screen) {
    font-size: $max-size;
  }
}
```

### Theme System
```scss
$themes: (
  light: (
    background: white,
    text: black,
    primary: #007bff
  ),
  dark: (
    background: #1a1a1a,
    text: white,
    primary: #0056b3
  )
);

@mixin themed() {
  @each $theme, $map in $themes {
    .theme-#{$theme} & {
      $theme-map: () !global;
      @each $key, $submap in $map {
        $value: map-get(map-get($themes, $theme), '#{$key}');
        $theme-map: map-merge($theme-map, ($key: $value)) !global;
      }
      @content;
      $theme-map: null !global;
    }
  }
}

@function themed($key) {
  @return map-get($theme-map, $key);
}
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install SASS globally
npm install -g sass

# Or use package.json
npm install --save-dev sass
```

### Compilation Commands
```bash
# Basic compilation
sass input.scss output.css

# Watch for changes
sass --watch sass_scss/:css/

# Compressed output
sass --style compressed input.scss output.css

# Source maps
sass --source-map input.scss output.css
```

### Development Workflow
```bash
# Project structure
project/
├── scss/
│   ├── abstracts/
│   │   ├── _variables.scss
│   │   ├── _functions.scss
│   │   └── _mixins.scss
│   ├── base/
│   │   ├── _reset.scss
│   │   └── _typography.scss
│   ├── components/
│   │   ├── _buttons.scss
│   │   └── _forms.scss
│   └── main.scss
└── css/
    └── main.css
```

## 🧪 Testing and Optimization

### Compilation Testing
```bash
# Test compilation
sass --check sass_scss/

# Dry run
sass --dry-run input.scss

# Verbose output
sass --verbose input.scss output.css
```

### Performance Optimization
```scss
// Avoid deep nesting (max 3-4 levels)
.component {
  .element {
    .sub-element {
      // Avoid going deeper
    }
  }
}

// Use placeholders for reusable styles
%clearfix {
  &::after {
    content: "";
    display: table;
    clear: both;
  }
}

// Optimize media queries
@mixin respond-to($breakpoint) {
  @if $breakpoint == mobile {
    @media (max-width: 767px) { @content; }
  }
  @if $breakpoint == tablet {
    @media (min-width: 768px) and (max-width: 1023px) { @content; }
  }
}
```

## 📚 Best Practices

### 1. Organization
- Use the 7-1 pattern for large projects
- Keep partials focused on single concerns
- Use consistent naming conventions

### 2. Performance
- Avoid unnecessary nesting
- Use placeholders over mixins when possible
- Minimize selector complexity

### 3. Maintainability
- Document complex mixins and functions
- Use semantic variable names
- Follow consistent code style

### 4. Scalability
- Create modular, reusable components
- Use maps for configuration
- Implement consistent design tokens

## 🎓 Learning Resources

### Official Documentation
- [SASS Official Guide](https://sass-lang.com/guide)
- [SCSS Syntax Reference](https://sass-lang.com/documentation)

### Advanced Tutorials
- [SASS Guidelines](https://sass-guidelin.es/)
- [The Sass Way](http://thesassway.com/)

### Tools and Extensions
- VS Code SASS extensions
- SASS linting tools
- Autoprefixer integration

---

*This module provides a solid foundation in SASS/SCSS, from basic concepts to advanced features, enabling you to write more efficient, maintainable, and powerful CSS for modern web development.*