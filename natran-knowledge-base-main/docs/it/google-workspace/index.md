# Google Workspace

The primary identity, communication and productivity suite. Windows sign-in, Microsoft access
and Keeping all derive from the Workspace account.

## Accounts

* [Admin privileges require a separate account](admin-account-separation.md) - No daily-driver account may hold admin privileges; elevated access uses a second, dedicated account.
* [Workspace account provisioning](account-provisioning.md) - Creating a user, the organizational unit structure, the onboarding steps that follow, and the employee info that feeds the email signature.
* [2-Step Verification](two-step-verification.md) - Checking whether a user has 2FA on, and the two routes to enabling it depending on account age.
* [Google Groups membership](google-groups.md) - Which groups populate automatically and which two require manual addition.
* [Microsoft 365 provisioning](microsoft-365-provisioning.md) - How Workspace users are automatically provisioned into Entra, how they sign in, and the deletion case needing manual cleanup.
* [Workspace account offboarding and backup](account-offboarding.md) - Locking a departing user out, taking a Takeout backup, deleting the account, and archiving the result.
* [Email forwarding for offboarded accounts](email-forwarding.md) - Keeping a departing user's address live, and the extra filter needed when forwarding into Keeping.

## Mail, contacts and signatures

* [Employee profile photo](profile-photo.md) - Photo requirements and the two places an employee photo must be uploaded.
* [Email signature deployment](email-signature-deployment.md) - Deploying a signature with GAM from the user's Workspace profile data, plus the Gmail defaults the user must set.
* [Email signature template structure](email-signature-template-structure.md) - How the template, placeholders, GAM command segments and conditional-removal tags fit together.
* [Keeping shared inbox setup](keeping-shared-inbox.md) - Inviting a user to Keeping, the setup they complete themselves, and what the Chrome extension does.
* [Group email moderation](group-email-moderation.md) - What a "Moderator's spam report" email means and how to approve or reject held messages.
* [Shared contacts administration](shared-contacts.md) - Granting and removing Shared Contacts licences, and managing contacts on shared labels.

## Security and tooling

* [Context-Aware Access](context-aware-access.md) - The access levels restricting Workspace to company-owned or approved password-protected devices, and how new policies are rolled out.
* [CAA device approval and troubleshooting](caa-device-approval.md) - What to do when a user hits the red "You don't have access" screen.
* [GAM setup and commands](gam-setup-and-commands.md) - What GAM is, its local directories, switching between the Natran and APS tenants, and the delegation commands in regular use.
