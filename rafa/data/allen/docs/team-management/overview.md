# Team management

Team management enhances collaboration within Ingka Engineering teams. Our solution introduces streamlined team management and simplified access control. These improvements aim to optimize team administration, ensuring a more seamless and efficient collaboration experience within Ingka Engineering teams.

An important note to make regarding our solution is that it is just an improved front for the existing teams [solution](https://confluence.build.ingka.ikea.com/pages/viewpage.action?spaceKey=EKR234IA&title=Team+Groups+in+Azure+AD){:target="\_blank"} from IAM.

<iframe id="kaltura_player" type="text/javascript" src='https://cdnapisec.kaltura.com/p/1848742/embedPlaykitJs/uiconf_id/53785772?iframeembed=true&entry_id=1_a4j796yl&config[provider]={"widgetId":"1_u73q26qn"}&config[playback]={"startTime":0}' style="width: 100%;height: auto;border: 0;aspect-ratio: 16 / 9;" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="Manage your teams in Allen"></iframe>

Navigate to the [homepage](https://allen.ingka.com){:target="\_blank"} and click on the ![Manage teams](../assets/team-mangement/manage_teams.png){: width="125px" align="middle" style="position: relative; bottom:5px"} button located in the top right corner

## Available Features

### **Team Creation**

Users can create new digital team groups and add members to it. The creator becomes the default owner, with the option to edit the team later by adding or removing owners and members.

**Note:** Member details are stored in **Azure AD (Microsoft Entra ID)** and Owner details are stored in **MyIdentity**.

### **Self-Service**

1. Join Team ![Join team icon](../assets/team-mangement/join_team.svg)

   - Users can request to join a team. The request is sent to the team owner for approval or rejection. Upon approval, the user is added to the requested team and updated in MyIdentity and Azure AD (Microsoft Entra ID) group. Approvals are managed through the [MyIdentity Portal](https://myidentity.apps.ikea.com/IdentityManager){:target="\_blank"}.

2. Unsubscribe from Team ![Unsubscribe team icon](../assets/team-mangement/remove_team.svg)

   - Users can request to leave a team. This is an auto-approval process, resulting in the user's removal from MyIdentity and Azure AD (Microsoft Entra ID) group.

### **Edit Team**

Team owners can edit teams by adding or removing owners and members. This includes an auto-approval process, updating MyIdentity and Azure AD (Microsoft Entra ID) groups after a successful request.

**Note:** Member details are stored in **Azure AD (Microsoft Entra ID)** and Owner details are stored in **MyIdentity**.

1. Add Owners

   - Owners can request to add new owners to a team.

2. Remove Owners

   - Owners can request to remove existing owners from a team.

3. Add Members

   - Owners can request to add new members to a team.

4. Remove Members

   - Owners can request to remove existing members from a team.

The following features are not available via Allen.

### **Delete Team**

As of now, the team owner can't delete a team via Allen, but it’s under discussion. Alternatively, you may try to raise a [NowIT](https://now.ingka.com/sp?id=sc_cat_item_guide&sys_id=0c69faf31b6ac950d9b1f7c4464bcbc8&sysparm_category=542cea410bc71510d9b1681b14f8dfa3){:target="\_blank"} ticket.

### **Connect Team to SMC System**

Please read [Connect Team to System](https://confluence.build.ingka.ikea.com/x/7zHOHw?){:target="\_blank"} confluence page.

## Support Channel

- [#allen-support](https://ikea.enterprise.slack.com/archives/C06EYSZJ0H4)

![Footer logo](../assets/team-mangement/footer_logo.png)
