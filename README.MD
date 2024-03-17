This directory containbs a subdirectory of each course in the LS curriculum. Each course directory, in turn, contains additional directories for each lesson or project in the course. There may be some classes in the future that require their own repository and those will be found outside of this one. The README file will be updated to list related courses and projects that are part of Core Curriculum but that are required to be a separate repo.
---
## Directory Breakdown

`ls-md`
The materials listed under the directory `ls-md` are all notes on the various topics covered. Notes here are not organized by class or lesson bu rather by concept. The best view of these is the local Obsidian vault for personal use.

*Class Directories*

The directory labeled with the class name, such as `py101`, contains exercises that are embedded in the course material, as well as projects.

There are several naminh conventions used for the comments in the repo, as well as branches. Conventions used in the comments are as folows:

## Naming Conventions
---
- `CH#-E additional comment` -- this denotes the chapter in a book, followed by the `E` tag, which indicates the push is releated to exercises, and lastly an additional comment if needed.

- `N`-- this indicates the commit pertains to notes. This type of commit is almost exclusively used in the `ls-ms` directory.

-`MP`-- Mastery Practice: this is the code used to identify commits that are related to material used to master fundamentals. This material is not necessarily related to any one class but rather to the mastery of the fundamental concepts presented in each course. Such as working through a long list of problems in the first two courses in preparation of the interviews. 

## Naming Convention for Branches
---

Branches have the following naming conventions:
- Quick Tests
    - `TV1` this naming convention startrs with `T` indicating it is a simple, quick test. If more than one is needed after the previous is deleted, the version number goes up, `TV1`, `TV2`, `TV3`, etc.
    - This naming convention will likely be used in exercises, where the change doesnt have major impact.

- `P` the `P` tag denotes that this is a project. Projects, like the mortgage calculator in `py101`, will have such branches.
    - `Ft` -- Feature
    - `Bug`-- Bug Fix

---

## Ful Example


|     Branch Name    |      Commit Tag + Comment                    |
| -------------------|:--------------------------------------------:|
| TV1-fibonacci      |    SM-E1 fibonacci sequence                  |
| PFt-mortgage-calc  |    PFt- adding rounding capability           |
| PBug-mortage-calc  |    PBug Fixing program bug with user input   |